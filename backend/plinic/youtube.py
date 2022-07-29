from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

'''
검색 단어를 받아 유튜브 링크를 반환
'''


DEVELOPER_KEY = "AIzaSyDfAxX1QZdRgBp5KUGpHXOjeYe8u9JX0hg"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search_list(word):
    '''
    "검색 단어" 를 인자로 받는다.
    최상위에 위치한 비디오 링크를 반환한다.
    '''
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        type="video",
        part="snippet",
        q=word,
        maxResults=1
    ).execute()

    # print(search_response)

    # Print the title and ID of each matching resource.
    for search_result in search_response.get("items", []):
        # pprint.pprint(search_result['id']['videoId'])
        return f'''{search_result['snippet']['title']} 
        youtube.com/watch?v={search_result['id']['videoId']}'''


if __name__ == "__main__":
    try:
        # pprint.pprint(youtube_search_list("원더풀"))
        temp = youtube_search_list(
            "TOTO +Toto")
        print(temp)
        tempList = list(map(str, temp.split()))
        print(tempList[-1])
    except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
