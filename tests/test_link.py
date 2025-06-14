import pytest

from scrapy.link import Link


class TestLink:
    def _assert_same_links(self, link1, link2):
        assert link1 == link2
        assert hash(link1) == hash(link2)

    def _assert_different_links(self, link1, link2):
        assert link1 != link2
        assert hash(link1) != hash(link2)

    def test_eq_and_hash(self):
        l1 = Link("http://www.example.com")
        l2 = Link("http://www.example.com/other")
        l3 = Link("http://www.example.com")

        self._assert_same_links(l1, l1)
        self._assert_different_links(l1, l2)
        self._assert_same_links(l1, l3)

        l4 = Link("http://www.example.com", text="test")
        l5 = Link("http://www.example.com", text="test2")
        l6 = Link("http://www.example.com", text="test")

        self._assert_same_links(l4, l4)
        self._assert_different_links(l4, l5)
        self._assert_same_links(l4, l6)

        l7 = Link(
            "http://www.example.com", text="test", fragment="something", nofollow=False
        )
        l8 = Link(
            "http://www.example.com", text="test", fragment="something", nofollow=False
        )
        l9 = Link(
            "http://www.example.com", text="test", fragment="something", nofollow=True
        )
        l10 = Link(
            "http://www.example.com", text="test", fragment="other", nofollow=False
        )
        self._assert_same_links(l7, l8)
        self._assert_different_links(l7, l9)
        self._assert_different_links(l7, l10)

    def test_repr(self):
        l1 = Link(
            "http://www.example.com", text="test", fragment="something", nofollow=True
        )
        l2 = eval(repr(l1))  # pylint: disable=eval-used
        self._assert_same_links(l1, l2)

    def test_bytes_url(self):
        with pytest.raises(TypeError):
            Link(b"http://www.example.com/\xc2\xa3")

     def test_nofollow_typecheck(self):
        with pytest.raises(TypeError):
            Link("http://www.example.com/", nofollow="Not a bool")
