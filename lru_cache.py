from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: str) -> str:
        if key not in self.cache:
            return ""
        self.cache.move_to_end(key)  # Обновляем порядок LRU
        return self.cache[key]

    def set(self, key: str, value: str) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # Обновляем порядок LRU
        elif len(self.cache) >= self.capacity:
            # Удаляем наименее используемый элемент
            self.cache.popitem(last=False)
        self.cache[key] = value

    def rem(self, key: str) -> None:
        self.cache.pop(key, None)


if __name__ == "__main__":
    cache = LRUCache(100)
    cache.set("Jesse", "Pinkman")
    cache.set("Walter", "White")
    cache.set("Jesse", "James")
    cache.get("Jesse")  # вернёт 'James'
    cache.rem("Walter")
    cache.get("Walter")  # вернёт ''
