from youtubesearchpython.core.constants import *
from youtubesearchpython.core.utils import *
from youtubesearchpython.extras import Video, Playlist, Suggestions, Hashtag, Comments, Transcript, Channel
from youtubesearchpython.search import Search, VideosSearch, ChannelsSearch, PlaylistsSearch, CustomSearch, \
    ChannelSearch
from youtubesearchpython.streamurlfetcher import StreamURLFetcher

__title__ = 'youtube-search-python'
__version__ = '1.6.2'
__author__ = 'alexmercerind'
__license__ = 'MIT'

''' Deprecated. Present for legacy support. '''
from youtubesearchpython.legacy import SearchVideos, SearchPlaylists
from youtubesearchpython.legacy import SearchVideos as searchYoutube
