import uvicorn
if __name__ == "__main__":
    # 启动虚拟环境
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)