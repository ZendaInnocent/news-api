import uvicorn

if __name__ == '__main__':
    uvicorn.run('server.app:app', reload=True, host='0.0.0.0', port=80)
