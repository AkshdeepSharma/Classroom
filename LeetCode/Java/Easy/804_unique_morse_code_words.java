class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        Set<String> hash_set = new HashSet<String>(); 
        String[] morse = {
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
            ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
            ".--","-..-","-.--","--.."
        };
        for(String word : words){
            StringBuilder sb = new StringBuilder();
            for(int i = 0; i < word.length(); i++){
                sb.append(morse[word.charAt(i) - 'a']);
            }
            hash_set.add(sb.toString());
        }
        return hash_set.size();
    }
}