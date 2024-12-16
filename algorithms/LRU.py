from pageReplacement import PageReplacement

class LRU(PageReplacement):
    def __init__(self, num_frames):
        super().__init__(num_frames)

    def access_page(self, page):
        if len(self.frames) < self.num_frames:
            if self.get_page(page.page_number) is None:
                self.frames.append(page)
            page.valid = True
        else:
            if self.get_page(page.page_number) is None:
                # 按LRU规则移除最久未使用的页面
                least_recently_used = min(self.frames, key=lambda p: p.last_access)
                self.frames.remove(least_recently_used)
                self.frames.append(page)
            page.valid = True
        page.last_access = 0  # 更新最近访问时间