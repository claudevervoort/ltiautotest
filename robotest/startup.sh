uvicorn main:app > log 2>&1 &
PID=$!
echo $PID > robotest_pid
