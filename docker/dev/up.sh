trap ctrl_c INT
function ctrl_c() {
        echo "** Trapped CTRL-C"
        docker-compose down
        exit
}
docker-compose down && docker-compose up
