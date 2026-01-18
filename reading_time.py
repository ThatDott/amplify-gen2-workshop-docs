#!/usr/bin/env python3
import os
import re

def count_words(text):
    # Remove markdown syntax and count words
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)  # Remove code blocks
    text = re.sub(r'`[^`]*`', '', text)  # Remove inline code
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)  # Remove images
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)  # Remove links, keep text
    text = re.sub(r'[#*_~`]', '', text)  # Remove markdown formatting
    words = text.split()
    return len(words)

def estimate_reading_time(word_count, wpm=200):
    return max(1, round(word_count / wpm))

def analyze_md_files(docs_path):
    total_words = 0
    files_analyzed = []
    
    for root, dirs, files in os.walk(docs_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    word_count = count_words(content)
                    reading_time = estimate_reading_time(word_count)
                    total_words += word_count
                    
                    rel_path = os.path.relpath(file_path, docs_path)
                    files_analyzed.append({
                        'file': rel_path,
                        'words': word_count,
                        'time': reading_time
                    })
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    
    return files_analyzed, total_words

if __name__ == "__main__":
    docs_path = "/amplify-gen2-workshop-docs-copy/docs"
    files, total_words = analyze_md_files(docs_path)
    
    print("📚 Markdown Files Reading Time Analysis")
    print("=" * 50)
    
    for file_info in sorted(files, key=lambda x: x['file']):
        print(f"{file_info['file']:<40} {file_info['words']:>4} words  {file_info['time']:>2} min")
    
    print("=" * 50)
    total_time = estimate_reading_time(total_words)
    print(f"{'TOTAL':<40} {total_words:>4} words  {total_time:>2} min")
    print(f"\nEstimated total reading time: {total_time} minutes ({total_time//60}h {total_time%60}m)")
