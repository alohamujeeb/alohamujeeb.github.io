---
hide:
  - navigation
  
tags:
  - Monkey patching
  - unit test
---

# Software Testing Techniques in Python



I think you've identified an important distinction that many books blur:

Developer testing (done while writing code)
Software/system testing (done after the software is assembled)

Monkey patching, mocking, fixtures, patching, parameterization, etc. are developer techniques. They are not testing types. They are mechanisms for writing tests.

If you're interested only in testing after the software is complete, then the list becomes much shorter and aligns with classical software engineering.

Test Type	Purpose
Unit Testing	Verify individual units/modules (often done during development, but still a formal test level)
Integration Testing	Verify modules work together
System Testing	Test the complete integrated software against requirements
Acceptance Testing (UAT)	Validate the software satisfies customer/business requirements
Regression Testing	Re-run tests after changes to ensure nothing broke

These five are the core test levels/types you'll find in industry.

Then there are specialized quality tests, which are not tied to a specific technology:

Performance Testing
Load Testing
Stress Testing
Scalability Testing
Security Testing
Usability Testing
Reliability Testing
Compatibility Testing
Recovery Testing

Notice that Monkey Patching, Mocking, Fixtures, Dependency Injection, etc. disappear completely because they are implementation techniques used primarily to enable unit and integration tests.

If I were writing a Python chapter

I'd separate it like this:

A. Software Test Types

Unit Testing
Integration Testing
System Testing
Acceptance Testing
Regression Testing

B. Python Testing Techniques

Monkey Patching
Mocking
Patching
Fixtures
Parameterized Tests
Property-Based Tests

That separation is much cleaner because it distinguishes what is being tested (software test levels) from how Python programmers implement those tests (testing techniques). Mixing those two categories is what causes most of the confusion.


---
## **Relevant Links**

[Python Material on this website](index.md)

