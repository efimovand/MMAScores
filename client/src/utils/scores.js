// Extract numbers from a string (e.g., "10 - 9" => [10, 9])
export const extractNumbers = (string) => {
    const nums = string.match(/\d+/g);
    return nums ? nums.map(n => parseInt(n, 10)) : [];
};

// Calculate rounds, sum, and winner from scores
export const calculateResults = (names, scores) => {
    const rounds = scores.map(extractNumbers);
    const sum = rounds.reduce((acc, round) => [acc[0] + round[0], acc[1] + round[1]], [0, 0]);
    const winner = sum[0] > sum[1] ? names[0] : sum[0] < sum[1] ? names[1] : 'Draw';
    return { rounds, sum, winner };
};
