# -*- coding: utf-8 -*-
# 多模式匹配算法AC自动机(Aho-Corasick Automaton)
# 摘自 https://www.cnblogs.com/en-heng/p/5247903.html


from collections import deque, namedtuple


IS_DEBUG = True
automaton = []
# state_id: int, value: char, goto: dict, failure: int, output: set
Node = namedtuple('Node', 'state value goto failure output')
print(Node.__doc__)  # Node(state, value, goto, failure, output)


def init_trie(words):
    """
    creates an AC automaton, firstly create an empty trie, then add words to the trie
    and sets fail transitions
    """
    create_empty_trie()
    # map(add_word, words)
    for w in words:
        add_word(w)
    set_fail_transitions()


def create_empty_trie():
    """ initialize the root of the trie """
    automaton.append(Node(0, '', {}, 0, set()))


def add_word(word):
    """add word into trie"""
    node = automaton[0]
    for char in word:
        # char is not in trie
        if goto_state(node, char) is None:
            next_state = len(automaton)
            node.goto[char] = next_state  # modify goto(state, char)
            automaton.append(Node(next_state, char, {}, 0, set()))
            node = automaton[next_state]
        else:
            node = automaton[goto_state(node, char)]
    node.output.add(word)


def goto_state(node, char):
    """goto function"""
    if char in node.goto:
        return node.goto[char]
    else:
        return None


def set_fail_transitions():
    """construction of failure function, and update the output function"""
    queue = deque()
    # initialization
    for char in automaton[0].goto:  # 添加toot节点的子节点
        s = automaton[0].goto[char]
        queue.append(s)
        automaton[s] = automaton[s]._replace(failure=0)
    while queue:
        r = queue.popleft()
        node = automaton[r]
        for a in node.goto:
            s = node.goto[a]  # node为当前节点，a为转移字符，s为当前节点的子节点
            queue.append(s)  # 添加当前节点的子节点
            # 从root节点的孙节点开始计算failure，因为所有root节点能goto到的状态，其failure函数值均为0。
            state = node.failure  # 使用子节点的上一节点即当前节点的failure
            # failure transition recursively
            # 子节点的上一节点即当前节点的failure状态通过转移字符goto
            while goto_state(automaton[state], a) is None and state != 0:  # goto失败，使用failure更新状态，继续goto
                state = automaton[state].failure
            # except the chars in goto function, all chars transition will goto root node self
            if state == 0 and goto_state(automaton[state], a) is None:
                goto_a = 0
            else:
                goto_a = automaton[state].goto[a]
            automaton[s] = automaton[s]._replace(failure=goto_a)  # 更新failure
            fs = automaton[s].failure
            automaton[s].output.update(automaton[fs].output)  # 更新output


def search_result(strings):
    """AC pattern matching machine"""
    result_set = set()
    node = automaton[0]
    for char in strings:
        while goto_state(node, char) is None and node.state != 0:  # goto失败，且不是根节点
            node = automaton[node.failure]
        if node.state == 0 and goto_state(node, char) is None:  # 当前在根节点，且goto失败  # 根节点goto失败不放在while循环里，防止死循环
            node = automaton[0]
        else:
            node = automaton[goto_state(node, char)]
        if len(node.output) >= 1:
            result_set.update(node.output)
    return result_set


if __name__ == '__main__':
    init_trie(['he', 'she', 'his', 'hers'])
    print(search_result('ushersm'))  # {'he', 'she', 'hers'}
