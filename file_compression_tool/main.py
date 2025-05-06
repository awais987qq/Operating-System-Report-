import argparse
from compress import compress_file
from integrity import verify_integrity

def main():
    parser = argparse.ArgumentParser(description="File Compression Tool")
    parser.add_argument("input", help="File or folder to compress")
    parser.add_argument("format", choices=["zip", "gzip"], help="Compression format")
    parser.add_argument("--output", help="Output file name", default=None)
    parser.add_argument("--level", choices=["fast", "best"], default="best", help="Compression level")
    parser.add_argument("--verify", action="store_true", help="Verify file integrity after compression")
    
    args = parser.parse_args()

    output_file = compress_file(args.input, args.format, args.output, args.level)

    if args.verify:
        original_ok = verify_integrity(args.input, output_file)
        print("Integrity:", "PASSED" if original_ok else "FAILED")

if _name_ == "_main_":
    main()