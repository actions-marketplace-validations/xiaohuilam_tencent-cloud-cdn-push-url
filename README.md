# Tencent Cloud CDN PUSH URLS Cache

This action will help you to push your CDN contents to edge nodes for Tencent Cloud CDN via its Python SDK API.

## Environment Variables

To use this Github action, you need to set the following environment variables in your workflow:

| Name | Description | Required |
| --- | --- | --- |
| SECRET_ID | your Tencent Cloud access token Secret ID | Yes |
| SECRET_KEY | your Tencent Cloud access token Secret Key | Yes |
| URLS | urls to push, separated with comma `,` | Yes |

## Example Usage

```yaml
uses: xiaohuilam/tencent-cloud-cdn-push-url@v1.2
env:
  SECRET_ID: ${{ secrets.TENCENTCLOUD_CDN_SECRET_ID }}
  SECRET_KEY: ${{ secrets.TENCENTCLOUD_CDN_SECRET_KEY }}
  URLS: "https://example.com/foo.html,https://example.com/bar.html"
```
