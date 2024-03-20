import fitz  
import csv

def extract_lines(start_pg, pdf_path):
    res = []
    pdf_document = fitz.open(pdf_path)
    for page_number in range(start_pg, len(pdf_document)):
        page = pdf_document.load_page(page_number)
        text = page.get_text()
        lines = text.splitlines()
        for line in lines:
            res.append(line)
    pdf_document.close()
    return res

def filter_lines(lines):
    new_lines = []
    for line in lines:
        words = line.split(' ')
        nwords = [word for word in words if word != '']
        nline = ' '.join(nwords)
        if nline != '':
            new_lines.append(nline)
    return new_lines

def get_groups_from_lines(lines):
    groups = []
    lst = []
    for line in lines:
        lst.append(line)
        if '@' in line:
            groups.append(lst)
            lst = []
    return groups

def get_info_from_group(group):
    return group[0], group[1], " ".join(group[2:-1]), group[-1]

def save_csv(data, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Company', 'Location', 'Email'])  # Write header row
        writer.writerows(data)

def main():
    pdf_path = input("Enter PDF file path: ")
    output_csv = input("Enter output CSV file path: ")
    lines = extract_lines(1, pdf_path)
    lines = filter_lines(lines)
    groups = get_groups_from_lines(lines)
    info_groups = [get_info_from_group(group) for group in groups]
    save_csv(info_groups, output_csv)

if __name__ == "__main__":
    main()