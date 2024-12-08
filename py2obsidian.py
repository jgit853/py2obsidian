import os
import shutil
from datetime import datetime
from typing import List, Set, Dict

class Py2Obsidian:
    """Main class for Python file archival to Obsidian vault."""
    
    def __init__(self, source_path: str, archive_path: str, obsidian_path: str):
        """Initialize paths and configurations.
        
        Args:
            source_path: Path to source Python files
            archive_path: Path for archiving files
            obsidian_path: Path to Obsidian vault
        """
        self.SOURCE_PATH = source_path
        self.ARCHIVE_PATH = archive_path
        self.OBSIDIAN_PATH = obsidian_path
        self.RESOURCES_PATH = os.path.join(self.OBSIDIAN_PATH, "300-Resources", "Python-Tools")
        
        # Default categories
        self.tool_categories = {
            'jsonc': 'Data-Processing',
            'packagelock': 'Data-Processing',
            'checkword': 'Text-Processing',
            'edjc': 'Text-Processing',
            '850dic': 'Data-Processing',
            'merge': 'Utility',
            'digit': 'Utility',
            'rpatxt': 'Text-Processing',
            'import': 'Utility',
            'claude': 'Utility'
        }

    def ensure_directories(self) -> None:
        """Create necessary directories if they don't exist."""
        directories = [
            os.path.join(self.RESOURCES_PATH, "Data-Processing"),
            os.path.join(self.RESOURCES_PATH, "Text-Processing"),
            os.path.join(self.RESOURCES_PATH, "Utility"),
            self.ARCHIVE_PATH
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            print(f"Created/confirmed directory: {directory}")

    def read_python_file(self, file_path: str) -> str:
        """Read Python file content with encoding handling."""
        encodings = ['utf-8', 'gbk']
        
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    return f.read()
            except UnicodeDecodeError:
                continue
        
        return "Unable to read file content, encoding issue detected."

    def create_markdown_doc(self, tool_name: str, original_path: str, 
                          archive_path: str, target_path: str) -> None:
        """Create Markdown documentation for the Python file."""
        doc_path = os.path.join(target_path, f"{tool_name}.md")
        code_content = self.read_python_file(original_path)
        current_time = datetime.now().strftime('%Y-%m-%d')
        current_time_full = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        content = self._generate_markdown_content(
            tool_name, archive_path, target_path, 
            code_content, current_time, current_time_full
        )
        
        with open(doc_path, 'w', encoding='utf-8') as f:
            f.write(content)

    def _generate_markdown_content(self, tool_name: str, archive_path: str,
                                target_path: str, code_content: str,
                                current_time: str, current_time_full: str) -> str:
        """Generate Markdown content with template."""
        return (
            f"---\n"
            f"type: python-tool\n"
            f"name: {tool_name}\n"
            f"created: {current_time}\n"
            f"last_used: {current_time}\n"
            f"archive_path: {archive_path}\n"
            f"tags: #python #tool\n"
            f"---\n\n"
            f"# {tool_name}\n\n"
            f"## File Information\n"
            f"- Archive Location: {archive_path}\n"
            f"- Creation Time: {current_time_full}\n\n"
            f"## Usage\n"
            f"Run in terminal: `python {tool_name}.py`\n\n"
            f"## Source Code\n"
            f"```python\n"
            f"{code_content}\n"
            f"```\n\n"
            f"## Description\n"
            f"[Add main functionality description here]\n\n"
            f"## Dependencies\n"
            f"- Python 3.x\n"
            f"- [Other dependencies]\n\n"
            f"## Update History\n"
            f"- {current_time}: Initial import\n"
        )

    def categorize_tool(self, tool_name: str) -> str:
        """Categorize tool based on name."""
        for key, category in self.tool_categories.items():
            if key.lower() in tool_name.lower():
                return category
        return 'Utility'

    def get_archived_files(self) -> Set[str]:
        """Get set of already archived files."""
        if not os.path.exists(self.ARCHIVE_PATH):
            return set()
        return set(os.listdir(self.ARCHIVE_PATH))

    def process_files(self) -> None:
        """Main processing function."""
        try:
            archived_files = self.get_archived_files()
            python_files = [f for f in os.listdir(self.SOURCE_PATH) if f.endswith('.py')]
            
            if not python_files:
                print("No Python files found!")
                return

            new_files = [f for f in python_files if f not in archived_files]
            
            if not new_files:
                print("No new Python files to process!")
                return

            print("\nProcessing files:")
            for py_file in new_files:
                self._process_single_file(py_file)

        except Exception as e:
            print(f"Error processing files: {str(e)}")

    def _process_single_file(self, py_file: str) -> None:
        """Process a single Python file."""
        try:
            tool_name = os.path.splitext(py_file)[0]
            category = self.categorize_tool(tool_name)
            target_path = os.path.join(self.RESOURCES_PATH, category)
            
            original_path = os.path.join(self.SOURCE_PATH, py_file)
            archive_file_path = os.path.join(self.ARCHIVE_PATH, py_file)
            
            shutil.copy2(original_path, archive_file_path)
            self.create_markdown_doc(tool_name, original_path, 
                                  archive_file_path, target_path)
            print(f"Processed: {py_file}")
            
        except Exception as e:
            print(f"Error processing {py_file}: {str(e)}")

def main():
    """Main entry point."""
    # Default paths - modify these as needed
    source_path = r"E:\bak\desktop"
    archive_path = r"G:\Bak\files\software\python-tools"
    obsidian_path = r"G:\Bak\OBSIDIAN\Vault111"
    
    archiver = Py2Obsidian(source_path, archive_path, obsidian_path)
    archiver.ensure_directories()
    archiver.process_files()

if __name__ == "__main__":
    main()
