## 本地阅读

### 构建gitbook镜像(可选)
下载本仓库后，执行`docker build . -t <image:tag>`构建自定义镜像，也可以直接使用我构建好的镜像`morso1/gitbook-server:3.2.3`

### 启动gitbook服务
```bash
cd llm-book

docker run --rm -v "$PWD/LLMProjects:/gitbook" -p 4000:4000 morso1/gitbook-server:3.2.3 gitbook serve
```
打开本地4000端口即刻阅读