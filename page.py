class Page:
    def __init__(self, page_number):
        self.page_number = page_number
        self.physical_block = None  # 空表示尚未分配物理块
        self.valid = False          # 状态位，表示是否在内存中
        self.last_access = None     # 记录最后访问时间（适用于 LRU 等算法）

    def __repr__(self):
        return f"Page {self.page_number} -> Block {self.physical_block}, Valid {self.valid}"