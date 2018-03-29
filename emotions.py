import abc


class Emotion(abc.ABCMeta):

    @abc.abstractmethod
    def name(cls):
        pass

    @abc.abstractmethod
    def hex_color(cls):
        pass

    @abc.abstractmethod
    def rgb_color(cls):
        pass

    @abc.abstractmethod
    def index(cls):
        pass


class Neutral(Emotion):

    def name(cls):
        return 'Neutral'

    def hex_color(cls):
        return '#000000'

    def rgb_color(cls):
        return 'rgb(0, 0, 0)'

    def index(cls):
        return 1


# TODO: Add colors
class Happy(Emotion):

    def name(cls):
        return 'Happy'

    def hex_color(cls):
        pass

    def rgb_color(cls):
        pass

    def index(cls):
        return 2

# TODO: Add colors
class Sad(Emotion):
    def name(cls):
        return 'Sad'

    def hex_color(cls):
        pass

    def rgb_color(cls):
        pass

    def index(cls):
        return 3


# TODO: Add colors
class Angry(Emotion):
    def name(cls):
        return 'Angry'

    def hex_color(cls):
        pass

    def rgb_color(cls):
        pass

    def index(cls):
        return 4


# TODO: Add colors
class Surprise(Emotion):
    def name(cls):
        return 'Surprise'

    def hex_color(cls):
        pass

    def rgb_color(cls):
        pass

    def index(cls):
        return 5


# TODO: Add colors
class Scared(Emotion):
    def name(cls):
        return 'Scared'

    def hex_color(cls):
        pass

    def rgb_color(cls):
        pass

    def index(cls):
        return 6


# TODO: Add colors
class Disgust(Emotion):
    def name(cls):
        return 'Disgust'

    def hex_color(cls):
        pass

    def rgb_color(cls):
        pass

    def index(cls):
        return 7