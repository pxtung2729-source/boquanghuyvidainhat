# X-Wave Server – Deploy trên Vercel

## Cấu trúc

```
x-wave-vercel/
├── api/
│   └── index.py         # FastAPI server (Vercel Serverless Function)
├── free/
│   ├── x-wave.txt       # Auth key
│   ├── lo.txt           # /MajorLogin khi đã xác thực
│   ├── locn.txt         # /MajorLogin khi chưa xác thực
│   ├── in.txt           # /fileinfo
│   ├── 3.txt            # /assetindexer
│   └── ph.txt           # /ver.php (JSON)
├── vercel.json
├── requirements.txt
└── .gitignore
```

## Bước 1 – Lấy file gốc từ server cũ

```bash
curl https://x-wave-server-ff.netlify.app/free/x-wave.txt -o free/x-wave.txt
curl https://x-wave-server-ff.netlify.app/free/lo.txt     -o free/lo.txt
curl https://x-wave-server-ff.netlify.app/free/locn.txt   -o free/locn.txt
curl https://x-wave-server-ff.netlify.app/free/in.txt     -o free/in.txt
curl https://x-wave-server-ff.netlify.app/free/3.txt      -o free/3.txt
curl https://x-wave-server-ff.netlify.app/free/ph.txt     -o free/ph.txt
```

## Bước 2 – Deploy lên Vercel

### Cách 1: Vercel CLI
```bash
npm i -g vercel
vercel
```

### Cách 2: GitHub
1. Push toàn bộ thư mục lên GitHub
2. Vào [vercel.com](https://vercel.com) → **Add New Project**
3. Import repo → bấm **Deploy**

## Bước 3 – Cập nhật Cloudflare Worker

```js
const AUTH_URL = "https://<your-app>.vercel.app/free/x-wave.txt";
const BASE_RESOURCE_URL = "https://<your-app>.vercel.app/free/";
```
