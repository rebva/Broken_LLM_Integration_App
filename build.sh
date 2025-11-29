cd ~/docker/Broken_LLM_Integration_App/chatapp
docker compose --env-file ./backend/.env build
docker compose --env-file ./backend/.env up
