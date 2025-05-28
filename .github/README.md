# Critical GHAS Security Alerts to Slack

This GitHub Action automatically notifies a Slack channel when:

- **Critical** Dependabot vulnerability alerts are detected
- Secret Scanning alerts are found (all considered critical)
- On a scheduled basis (every Monday) to provide a summary of critical alerts
- When new critical security events are detected after a push

## Setup Instructions

### 1. Create a Slack Webhook

1. Go to [Slack API Apps](https://api.slack.com/apps)
2. Click "Create New App" → "From scratch"
3. Give your app a name and select your workspace
4. Click "Incoming Webhooks" and activate the feature
5. Click "Add New Webhook to Workspace"
6. Select the channel where you want to receive notifications
7. Copy the Webhook URL

### 2. Add the Webhook URL to GitHub Secrets

1. In your GitHub repository, go to Settings → Secrets → Actions
2. Click "New repository secret"
3. Name: `SLACK_WEBHOOK_URL`
4. Value: Paste the webhook URL you copied from Slack
5. Click "Add secret"

### 3. Enable GitHub Advanced Security Features (for organization repositories)

For this workflow to access Dependabot and secret scanning alerts:

1. Make sure GitHub Advanced Security is enabled for your repository
   - Go to Settings → Security & analysis
   - Enable Dependabot alerts and Secret scanning

2. Ensure the workflow has appropriate permissions
   - The workflow uses `GITHUB_TOKEN` which should have read access to security events by default

## How It Works

The workflow will:

1. Trigger on:
   - Scheduled runs (every Monday at 9:00 AM UTC)
   - Manual triggers (workflow_dispatch)
   - Push events to detect new security issues

2. Collect only critical alerts from:
   - Dependabot vulnerability alerts (severity: critical)
   - Secret scanning (all considered critical)

3. Format and send the alerts to your specified Slack channel

## Security Focus

This workflow focuses **only on critical security issues**, ensuring that:

- You're not overwhelmed with non-critical alerts
- Your team can respond quickly to the most important security issues
- Secret leaks and critical vulnerabilities get immediate attention

## Customization

You can customize this workflow by:

- Changing the schedule in the `cron` expression
- Modifying the Slack message format in the `payload` section
- Adding additional event triggers as needed

## Troubleshooting

If you're not receiving notifications:

1. Check that your Slack webhook URL is correctly configured in the repository secrets
2. Verify that GitHub Advanced Security features are enabled for your repository
3. Check the workflow run logs for any errors that might indicate permission issues
