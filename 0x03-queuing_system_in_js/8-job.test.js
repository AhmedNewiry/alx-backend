import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  after(() => {
    queue.testMode.exit();
    queue.testMode.clear();  // Clear jobs in test mode
  });

  it('should display an error message if jobs is not an array', () => {
    const badJobs = 'not an array';
    try {
      createPushNotificationsJobs(badJobs, queue);
    } catch (error) {
      expect(error.message).to.equal('Jobs is not an array');
    }
  });

  it('should create two new jobs in the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518743',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518782',
        message: 'This is the code 4321 to verify your account',
      },
    ];
    createPushNotificationsJobs(jobs, queue);

    const jobsInQueue = queue.testMode.jobs;
    expect(jobsInQueue).to.have.lengthOf(2);
    expect(jobsInQueue[0].type).to.equal('push_notification_code_3');
    expect(jobsInQueue[1].type).to.equal('push_notification_code_3');
  });
});
