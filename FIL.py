import PyPDF2
import re
#НАСИЛИЕ УБИЙСТВА АААААААА
def search_in_pdf(filename, search_query):
    found_texts = []
    search_query = search_query.lower()
    
    with open(filename, 'rb') as file:
        rUS2 = PyPDF2.PdfReader(file)
    
        for page_num in range(len(rUS2.pages)):
            page = rUS2.pages[page_num]
            text = page.extract_text()
            
            if text and search_query in text.lower():
                SEXS = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
                for SEX in SEXS:
                    if search_query in SEX.lower():
                        found_texts.append({
                            'file': filename,
                            'page': page_num + 1,
                            'text': SEX.strip()
                        })
    
    return found_texts
#НАСИЛИЕ УБИЙСТВА АААААААА
def FILPIKA():
    pdf_files = ['111.pdf']
    print("Доступные файлы для поиска:", ", ".join(pdf_files))
    
    while True:
        query = input("\nВведите тему или фразу для поиска (или 'выход' для завершения): ").strip()
        if query.lower() == 'выход':
            break
            
        if not query:
            print("Пожалуйста, введите запрос.")
            continue
            
        DD = []
        for pdf_file in pdf_files:
            try:
                FF = search_in_pdf(pdf_file, query)
                DD.extend(FF)
            except FileNotFoundError:
                print(f"Файл {pdf_file} не найден!")
                continue
                
        if not DD:
            print("Ничего не найдено. Попробуйте другой запрос.")
        else:
            print(f"\nНайдено {len(DD)} результатов:")
            for i, FF in enumerate(DD, 1):
                print(f"\nРезультат {i}:")
                print(f"Файл: {FF['file']}")
                print(f"Страница: {FF['page']}")
                print(f"Текст: {FF['text']}")
FILPIKA()
