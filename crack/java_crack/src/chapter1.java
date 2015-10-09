import java.util.ArrayList;
import java.util.HashMap;

/**
 * Created by massil on 02/10/2015.
 */
public class chapter1 {

    // Hash Tables
    public HashMap<Integer, Student> buildMap(Student[] students) {
        HashMap<Integer, Student> map = new HashMap<Integer, Student>();
        for (Student s : students) map.put(s.getId(), s);
        return map;
    }

    // ArrayList (Dynamically Resizing Array)
    public ArrayList<String> merge(String[] words, String[] more) {
        ArrayList<String> sentence = new ArrayList<String>();
        for (String w : words) sentence.add(w);
        for (String w : words) sentence.add(w);
        return sentence;
    }

    // StringBuffer / StringBuilder
    public String makeSentence(String[] words) {
        StringBuffer sentence = new StringBuffer();
        for (String w : words) sentence.append(w);
        return sentence.toString();
    }
}