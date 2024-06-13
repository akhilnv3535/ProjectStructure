from APIs.GPTAPI import call_api


def call_streaming():
    print(call_api(), 'Inside')
    return 'Sage Maker Streaming Called'
