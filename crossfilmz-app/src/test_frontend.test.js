// command to include code coverage report
// yarn test --coverage --passWithNoTests

// Expects documented here
// https://jestjs.io/

test("Primitive equals", () => {
	expect(800).toBe(800);
	// toBe is for primitive types
});

test("Object equals", () => {
	expect({ x: 20, y: 20 }).toEqual({ x: 20, y: 20 });
	// toEqual is for reference types/arrays 'n stuff
});