import random


class Table(object):
    def __init__(self, n):
        self.buckets = {}  # 创建一个字典用来存放一个拥有n个桶的哈希表
        self.bucket_num = n  # 表示当前桶个数
        # 循环为字典内添加n个桶
        for key in range(n):
            key = str(key)
            self.buckets.update({key: []})

    def add(self, hash_key, value):
        """
        在表中添加新元素
        :param hash_key:新元素的哈希值
        :param value:新元素的值
        """
        key = hash_key % len(self.buckets)  # 通过取余计算确定元素应存在的桶
        key = str(key)
        self.buckets[key].append(value)  # 将元素添加进其所属的桶列表

    def get(self, hash_key):
        """
        获取表中的元素
        :param hash_key: 想要获取的元素的哈希值
        :return: # 返回元素所在的桶列表
        """
        key = hash_key % len(self.buckets)  # 通过取余计算确定元素应存在的桶
        key = str(key)
        return self.buckets[key]


class HashTable(object):
    def __init__(self):
        self.table = Table(2)  # 初始化表,表初始容量为2
        self.num = 0  # 哈希表中的数据条数

    def add(self, value):
        """
        # 向表中添加元素
        :param value: 想要添加的元素
        """
        if self.num == self.table.bucket_num:
            # 若当前数据量已超过桶数量,则先将原有数据重新排列,而后添加新元素
            self.rehash()
        hash_key = hash(value)
        self.table.add(hash_key, value)
        self.num += 1

    def get(self, value):
        """
        # 获取表中的元素
        :param value: 想要获取的元素
        :return: 元素所在的桶列表
        """
        hash_key = hash(value)
        return self.table.get(hash_key)

    def rehash(self):
        """
        #将哈希表重新排列
        """
        # 创建一个新的表,桶的数量是之前表的二倍
        new_table = Table(self.table.bucket_num * 2)
        # 遍历之前的表,将其中元素添加到新表中
        for key in self.table.buckets:
            for value in self.table.buckets[key]:
                hash_key = hash(value)
                new_table.add(hash_key, value)
        self.table = new_table


class UnitTest(object):
    def __init__(self):
        self.hash_table = HashTable()

    def get_input(self):
        """
        获取测试数据
        :return: 字符串型,最大长度为1024的以8位为一段的二进制ascii码
        """
        num = ''
        count = random.randint(1, 1024 / 8)  # 获得随机的段落数量
        for time in range(count * 8):
            num += str(random.randint(0, 1))  # 添加段落相应位数的二进制字符
        return num

    def count_test(self, count):
        """
        通过递归进行对哈希表的指定次数的测试
        :param count: 想要测试的数据量
        """
        num = self.get_input()
        self.hash_table.add(num)
        if count > 1:
            count -= 1
            self.count_test(count)
        get = self.hash_table.get(num)  # 测试值的获取
        print(get)  # 在控制台输出获取到的列表
        if num in get:
            print(True)  # 若测试值存在于获取到的列表中,则在控制台中输出True

    def ut(self, count):
        """
        对哈希表的单元内部测试
        :param count: 测试的次数
        :return:测试后的哈希表对象
        """
        self.count_test(count)
        print(self.hash_table.table.buckets)  # 在控制台输出测试后的哈希表
        for item in self.hash_table.table.buckets:
            print('%8s,%3s' % (item, str(len(self.hash_table.table.buckets[item]))))  # 在控制台输出测试后的哈希表所有的键与其对应的值数量
        return self.hash_table


if __name__ == '__main__':
    # 实现一个hash table，input数据是最长1024的ascii码
    unit_test = UnitTest()
    unit_test.ut(11)  # 指定测试数据的数量
    # 测试数据为字符串型,最大长度为1024的以8位为一段的二进制ascii码
    # 测试数据随机生成,添加到哈希表中后,对数据进行查找,控制台输出查找到的结果列表,若测试数据存在于结果列表中,则于结果列表下一行输出True
    # 测试数据添加查询结束后,整体输出哈希表
    # 而后在控制台输出测试后的哈希表所有的键,和每个键所对应的值列表的长度
