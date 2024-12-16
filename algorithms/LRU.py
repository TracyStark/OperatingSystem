from pageReplacement import PageReplacement

class LRU(PageReplacement):
    def __init__(self, num_frames):
        super().__init__(num_frames)

    def access_page(self, page):
        if len(self.frames) < self.num_frames:
            if self.get_page(page.page_number) is None:
                page.physical_block = len(self.frames)  # 分配物理块号
                self.frames.append(page)
                page.valid = True
                print(f"Page {page.page_number} caused a page fault and was added to memory.")
            else:
                print(f"Page {page.page_number} is already in memory.")
        else:
            if self.get_page(page.page_number) is None:
                # 按LRU规则移除最久未使用的页面
                least_recently_used = min(self.frames, key=lambda p: p.last_access)
                page.physical_block = least_recently_used.physical_block  # 继承被替换页面的物理块号
                self.frames.remove(least_recently_used)
                self.frames.append(page)
                page.valid = True
                print(f"Page {page.page_number} caused a page fault and replaced page {least_recently_used.page_number}.")
            else:
                print(f"Page {page.page_number} is already in memory.")
        page.last_access = 0  # 更新最近访问时间
        self.print_page_table()

    def print_page_table(self):
        print("Current Page Table:")
        for frame in self.frames:
            print(frame)