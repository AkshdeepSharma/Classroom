const checkIfPangram = sentence => {
    const characters = new Set();
    for(let i=0; i < sentence.length; i++)
        characters.add(sentence[i]);
    return characters.size === 26;
};