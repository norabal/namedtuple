"""
namedtupleを使って辞書的なデータセットを作りたい。
環境はpython 3.6以下。
一度定義すれば変更されづらいし、可読性が良い。

3.7だとdataclassesを使うことでよりカスタマイズが効くようになるとのこと。

参考にさせていただいたQiita記事様:　https://qiita.com/tag1216/items/19fbc1a4f6a24dd7861b
"""

from collections import namedtuple

ITEM = namedtuple('item', ('title', 'url', 'user', 'body'))
ITEM_SET = (
    ITEM(title='item1', url='http:example.com/item1', user='user1', body='body1'),
    ITEM(title='item2', url='http:example.com/item2', user='user2', body='body2'),
    ITEM('item3', None, 'user2', True)  # 属性名は省いてしまってもOK。
)

def main():

    # namedtupleのフィールドをタプルで表示
    print(ITEM._fields)

    user = 'user'
    for s in ITEM_SET:
        print(s[0])  # インデックスでアクセス
        print(s.body)  # 属性名でアクセス

        # 変数を使ってアクセス
        try:
            print(s[user])
        except TypeError as err:
            print('dictで可能なこのアクセス方法はできない{}'.format(err))

        # getattrなら大丈夫
        print(getattr(s, user))

    # 値の変更を試す
    try:
        ITEM_SET[1].title = 'very cool title'
    except AttributeError as err:
        print('タプルはimmutable（不変）なので変更はできない: {}'.format(err))

    # jsonに変換も簡単
    import json
    print(json.dumps(ITEM_SET))


if __name__ == '__main__':
    main()
