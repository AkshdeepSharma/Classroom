const numRescueBoats = (people, limit) => {
    let i = 0;
    let j = people.length - 1;
    let numBoats = 0;
    people.sort((a, b) => a - b);
    while(i <= j){
        if(i === j){
            i++;
        } else if(people[i] + people[j] <= limit){
            i++;
            j--;
        } else if(people[i] + people[j] > limit){
            j--;
        }
        numBoats++;
    }
    return numBoats;
};