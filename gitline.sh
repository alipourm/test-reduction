for c in $(git log -G "gcov_exec" --format=%H -- ../src/main/java/edu/oregonstate/starg/TestCase.java); do
    git --no-pager grep -e "gcov_exec" $c -- ../src/main/java/edu/oregonstate/starg/TestCase.java
done