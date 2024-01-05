const express = require('express');
const math = require('mathjs');

const app = express();
const port = 5000;

app.get('/numericalintegralservice/:lower/:upper', (req, res) => {
	const lower = parseFloat(req.params.lower);
	const upper = parseFloat(req.params.upper);

	const iterations = [10, 100, 1000, 10000, 100000, 1000000];
	const results = [];

	iterations.forEach((N) => {
		const delta_x = (upper - lower) / N;
		let result = 0.0;

		for (let i = 0; i < N; i++) {
			const x_i = lower + i * delta_x;
			result += Math.abs(math.sin(x_i)) * delta_x;
		}

		results.push({N, result});
	});

	res.json(results);
});

app.listen(port, () => {
	console.log(
		`Numerical Integration Microservice listening at http://localhost:${port}`
	);
});
