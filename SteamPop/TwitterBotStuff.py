from time import sleep
import config

while True:
    config.api.update_status('The most popular game among ' + '<user>' +  ' and their friends is ' + '<game>' + ' with <hours> played!')
    sleep(60 * 60 *12)