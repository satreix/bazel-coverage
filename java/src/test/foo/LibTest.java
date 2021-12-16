package foo;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class LibTest {
    @Test
    public void tooAdd() {
        Lib l = new Lib();
        assertEquals(5, l.add(1, 4));
    }
}
