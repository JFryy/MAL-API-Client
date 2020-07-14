import collections


class JsonResponse(object):
    """ Helper class for returning objects for nested dictionaries in API Response. """

    def __init__(self, d):
        self.d = d
        for a, b in d.items():
            a = a.replace('-', '_')
            if isinstance(b, (list, tuple)):
                setattr(
                    self, a,
                    [JsonResponse(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, JsonResponse(b) if isinstance(b, dict) else b)

    def __str__(self):
        if self.d:
            if isinstance(self.d, collections.abc.Iterable):
                return str(self.d)