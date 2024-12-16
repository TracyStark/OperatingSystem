from pageReplacement import PageReplacement

class FIFO(PageReplacement):
    def __init__(self, num_frames):
        super().__init__(num_frames)
        self.queue = []  # 用队列来实现FIFO

    def access_page(self, page):
        if len(self.frames) < self.num_frames:  # 如果内存未满
            if self.get_page(page.page_number) is None:
                page.physical_block = len(self.frames)  # 分配物理块号
                self.frames.append(page)  # 加入内存
                self.queue.append(page)  # 入队
                page.valid = True
                print(f"Page {page.page_number} caused a page fault and was added to memory.")
            else:
                print(f"Page {page.page_number} is already in memory.")
        else:
            # 内存已满，进行页面替换
            if self.get_page(page.page_number) is None:
                evicted = self.queue.pop(0)  # 按FIFO规则移除最旧页面
                page.physical_block = evicted.physical_block  # 继承被替换页面的物理块号
                self.frames.remove(evicted)
                self.frames.append(page)
                self.queue.append(page)
                page.valid = True
                print(f"Page {page.page_number} caused a page fault and replaced page {evicted.page_number}.")
            else:
                print(f"Page {page.page_number} is already in memory.")
        self.print_page_table()

    def print_page_table(self):
        print("Current Page Table:")
        for frame in self.frames:
            print(frame)