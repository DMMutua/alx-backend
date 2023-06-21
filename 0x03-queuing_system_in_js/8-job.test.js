import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    // Create a new queue with test mode
    queue = kue.createQueue({ testMode: true });
  });

  afterEach(() => {
    // Clear the queue and exit test mode
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('displays an error message if jobs is not an array', () => {
    const invalidJobs = 'invalid'; // Not an array
    expect(() => {
      createPushNotificationsJobs(invalidJobs, queue);
    }).to.throw('Jobs is not an array');
  });

  it('creates new jobs in the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Check the number of jobs in the queue
    expect(queue.testMode.jobs.length).to.equal(2);

    // Check the job data in the queue
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });

  // Add more test cases as needed
});

