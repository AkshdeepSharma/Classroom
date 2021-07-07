const checkRecord = s => {
    if((s.match(/A/g)||[]).length > 1 || (s.match(/LLL/g)||[]).length > 0){
        return false;
    }
    return true;
};