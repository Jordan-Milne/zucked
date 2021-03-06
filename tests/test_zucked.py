import zucked as zd

def test_top_words():
    top_words = [('hi', 3), ('lol', 2), ('i', 2), ('one', 1)]
    ms = zd.read_messages
    assert ms.top_words('Jordan Milne') == top_words

def test_stop_words():
    stop_words = [('hi', 3), ('lol', 2), ('one', 1)]
    ms = zd.read_messages
    assert ms.top_words('Jordan Milne',False) == stop_words

def test_top_convos():
    top_convo = [('Zark Muckerberg', 1)]
    ms = zd.read_messages
    assert ms.top_convos('Jordan Milne') == top_convo

# this test below passed locally but failed a lot on travis. I finally realized that the virtual machine travis-ci
# uses to test code is in a different timezone setting and was reading the timestamp_ms as a different time, failing the test.
def test_search_messages():
    search = [{'Message': 'hi hi hi lol lol one i i',
               'Sent to': 'Zark Muckerberg',
               'Date': '2020-05-11 15:59:15'}]
    ms = zd.read_messages
    assert ms.search_messages('Jordan Milne','one') == search


def test_format_top_words():
    format_words_output = {'2020': {'hi': 3, 'i': 2, 'love': 0, 'data': 0}}
    ms = zd.read_messages
    assert ms.format_top_words('Jordan Milne',['i','love','data','hi'],'2020') == format_words_output
