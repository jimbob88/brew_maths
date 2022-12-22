# brew_maths

The following is a python module designed for simple recipe calculations. It is designed to be a new system that eventually Wheeler's Wort Works will
move to. If you have looked at the code for Wheeler's Wort Works, one can see a lot of issues in the design and philosophy. It was designed across a
long time period when I was younger, and it has become very difficult to develop for and fix... I am hoping that this module will let me port a lot of
the current functionality of Wheeler's Wort Works into a new system that does not rely on the old systems of the past. This will mean a complete
separation of business logic and user interface design, meaning it will be much easier to update and fix. Having this as a separate module should also
help others create their own recipe software.

## Contributing

If you have another formula, or some code you would like to add, feel free to open up an issue and give an example of its usecase. This way we can
massively expand the available formulas, and so help others make their code work.

## Thanks

- To Graham Wheeler for all his contributions to the Brewing Community.
- To the team on [brewtarget](https://github.com/Brewtarget/brewtarget)
- To my Dad for answering all my brewing questions
- To all the people who have contributed to JimsBeerKit
- And many more!

### Glossary

```
ABV - Alcohol by Volume
Brewer's Degrees - Alternatively: Excess Gravity. For example, 1.045 -> 45
Final Gravity - Alternatively: Present Gravity, Specific Gravity.
```