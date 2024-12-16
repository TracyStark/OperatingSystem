from page import Page  # 导入 Page 类
from algorithms.OPT import OPT  # 导入 OPT 算法类

def evaluate_performance(algorithm, access_sequence):
    page_faults = 0
    for i, page_num in enumerate(access_sequence):
        page = Page(page_num)
        future_pages = access_sequence[i + 1:]  # 获取当前页面之后的所有页面作为未来页面
        
        if isinstance(algorithm, OPT):  # 仅当是 OPT 算法时，传递 future_pages
            # 使用 get_page_with_future 而不是 access_page
            algorithm.get_page_with_future(page, future_pages)
            if algorithm.get_page(page.page_number) is None:
                page_faults += 1
        else:
            if algorithm.get_page(page.page_number) is None:
                page_faults += 1
            algorithm.access_page(page)
        
        print(f"Accessed Page {page.page_number}: {page}")
    return page_faults