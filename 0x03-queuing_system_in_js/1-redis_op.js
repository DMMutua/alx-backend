import redis from 'redis';

// Creating Redit Client Instance
const client = redis.createClient();

// Event handling
client.on('connect', () => {
        console.log('Redis client connected to the server');
});

client.on('error', (error) => {
        console.error(`Redis client not connected to the \
                server: ${error.message}`);
});


function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
	client.get(schoolName, (error, value) => {
		if (error) {
			console.error(`Error retrieving value \
				for ${schoolName}: ${error.message}`);
		}
		console.log(`${value}`);
	});
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
