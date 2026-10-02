import os
import sqlite3

def build_neural_law_database():
    print("⚡ Igniting Neural Ingestion Engine...")
    
    base_dir = r"C:\HVF_Repos\ultimate-law-private\The_Written_Word"
    db_path = os.path.join(base_dir, "ultimate_law.db")
    
    # Connect to (or create) the dedicated Ultimate Law brain sector
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Forging the memory schema
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scriptures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_text TEXT,
            passage TEXT
        )
    """)
    
    # Clear old memory if re-running
    cursor.execute("DELETE FROM scriptures")
    
    folders_to_scan = ["English_Core", "Original_Greek"]
    total_chunks = 0
    
    for folder in folders_to_scan:
        folder_path = os.path.join(base_dir, folder)
        if not os.path.exists(folder_path):
            continue
            
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(folder_path, filename)
                print(f"🧠 Ingesting: {filename}...")
                
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                
                # Chop the massive text into logical paragraphs/verses
                chunks = [chunk.strip() for chunk in content.split('\n\n') if len(chunk.strip()) > 20]
                
                for chunk in chunks:
                    cursor.execute("INSERT INTO scriptures (source_text, passage) VALUES (?, ?)", (filename, chunk))
                    total_chunks += 1
    
    conn.commit()
    conn.close()
    print(f"✅ INGESTION COMPLETE: {total_chunks} passages successfully mapped into Ebony's neural database.")

if __name__ == "__main__":
    build_neural_law_database()
