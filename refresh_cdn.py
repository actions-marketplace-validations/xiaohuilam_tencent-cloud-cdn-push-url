from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdn.v20180606 import cdn_client, models
import json
import os


def refresh_cdn(secret_id, secret_key, urls):
    cred = credential.Credential(secret_id, secret_key)
    http_profile = HttpProfile()
    http_profile.endpoint = "cdn.tencentcloudapi.com"

    client_profile = ClientProfile()
    client_profile.httpProfile = http_profile
    client = cdn_client.CdnClient(cred, "", client_profile)

    req = models.PushUrlsCacheRequest()
    chunk_urls = list(chunks(urls, 500))
    for _urls in chunk_urls:
        params = {
            "Urls": _urls,
        }
        params = json.dumps(params)
        req.from_json_string(params)
        client.PushUrlsCache(req)

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def parse_env():
    secret_id = os.getenv("TENCENTCLOUD_CDN_SECRET_ID", None)
    assert secret_id is not None, "Please provide Secret ID"
    secret_key = os.getenv("TENCENTCLOUD_CDN_SECRET_KEY", None)
    assert secret_key is not None, "Please provide Secret Key"
    urls = os.getenv("URLS", "")
    # split and only keep non-whitespaces
    urls = filter(lambda pth: len(pth) > 0, map(str.strip, urls.split(",")))
    urls = list(urls)
    assert len(urls) >= 1, "Please specify at least one url to pre-fetch"
    return secret_id, secret_key, urls

if __name__ == '__main__':
    try:
        refresh_cdn(*parse_env())
        print("Successfully prefetchd!")
    except TencentCloudSDKException as err:
        print("Failed to prefetch:")
        print(err)
        exit(-1)
