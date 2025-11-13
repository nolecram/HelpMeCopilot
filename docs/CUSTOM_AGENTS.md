# Custom GitHub Copilot Agents

This repository includes custom GitHub Copilot Agents that provide specialized assistance for specific tasks. These agents are configured to help with code quality, reliability, and operational excellence.

## Available Agents

### 1. Italian Commenting Agent
**Location**: `.github/agents/my-agent.agent.md`

**Purpose**: Adds clear, concise comments in Italian to code where they would improve readability and understanding.

**Capabilities**:
- Analyzes code to understand functionality
- Identifies documentation gaps
- Adds professional Italian comments explaining complex logic, functions, and business logic
- Follows existing code style and comment conventions

**Use Cases**:
- Documenting complex algorithms in Italian
- Adding function/method documentation
- Explaining non-obvious code patterns
- Providing context for business logic

### 2. SRE Agent (Site Reliability Engineering)
**Location**: `.github/agents/sre-agent.agent.md`

**Purpose**: Expert Site Reliability Engineer providing comprehensive guidance for all applications and infrastructure in this repository.

**Capabilities**:

#### Reliability & Resilience
- Error handling and exception management review
- Retry logic with exponential backoff recommendations
- Circuit breaker pattern implementation
- Graceful degradation strategies
- Health check endpoint verification
- Timeout configuration analysis
- Rate limiting recommendations

#### Performance & Scalability
- Resource efficiency analysis
- Caching strategy recommendations
- Database optimization and connection pooling
- Asynchronous operation identification
- Auto-scaling configuration review
- Load balancing verification
- Performance metrics identification

#### Security Best Practices
- Secrets management (no hardcoded credentials)
- Input validation and sanitization
- Authentication and authorization review
- Encryption (TLS/SSL, data at rest)
- Dependency vulnerability scanning
- Container security best practices
- IAM and least privilege principle
- Security headers for web applications

#### Observability & Monitoring
- Structured logging implementation
- Key metrics tracking (latency, errors, saturation, traffic)
- Distributed tracing recommendations
- Meaningful alerting with appropriate thresholds
- Dashboard visualization suggestions
- Log aggregation strategies
- APM integration recommendations

#### Infrastructure as Code
- Terraform best practices (modules, state, variables)
- Idempotency verification
- Disaster recovery and backup mechanisms
- Environment parity (dev/staging/production)
- Resource tagging for cost tracking
- Network security (security groups, ACLs, firewalls)
- High availability configurations

#### Container & Orchestration
- Docker best practices (multi-stage builds, minimal images, non-root users)
- Docker Compose service dependencies and networking
- Resource limits (CPU and memory)
- Image versioning (avoid "latest" tags)
- Container health checks
- Restart policies

#### Incident Response & SLOs
- Incident runbook creation
- SLI/SLO definition
- Error budget tracking
- Blameless postmortem culture
- Rollback strategy implementation
- Feature flag recommendations

**Use Cases**:
- Reviewing Python Flask applications for reliability
- Analyzing Terraform infrastructure configurations
- Improving Docker Compose setups
- Security audits of applications and infrastructure
- Performance optimization recommendations
- Implementing observability best practices
- Preparing for production deployments

## How to Use Custom Agents

### Using with GitHub Copilot

1. **In GitHub.com**: When viewing code or creating issues/PRs, you can reference agents in comments or descriptions
2. **In VS Code**: Use GitHub Copilot Chat and reference the agent by mentioning its expertise area
3. **In CLI**: Use the GitHub CLI with Copilot extensions to invoke agents

### Example Workflows

#### Code Review with SRE Agent
```bash
# Request SRE review of a Flask application
@copilot Please have the SRE agent review src/ExcuseGenerator/app.py 
for reliability and security best practices
```

#### Documentation with Italian Agent
```bash
# Add Italian comments to a Python file
@copilot Please have the Italian Commenting agent add helpful 
Italian comments to src/temperature_converter.py
```

#### Infrastructure Review
```bash
# Review Terraform configuration
@copilot Please have the SRE agent analyze 
src/ICA_Azure_AWS/lamp_stack_azure/ for security and reliability issues
```

## Creating Your Own Custom Agent

To create a new custom agent:

1. Create a new file in `.github/agents/` with the naming pattern: `agent-name.agent.md`

2. Use the following structure:
```markdown
---
name: Your Agent Name
description: Brief description of what the agent does
---

# Agent Name

Detailed instructions for the agent including:
- Role and expertise
- Responsibilities
- Guidelines
- Output format
- Examples
```

3. Commit the file to the default branch (main)

4. The agent will be available for use in GitHub Copilot

## Agent Configuration Format

Each agent file follows the GitHub Custom Agents specification:

- **Front Matter** (YAML): Contains `name` and `description`
- **Instructions**: Detailed markdown content explaining the agent's role, responsibilities, and behavior
- **Examples**: Code examples showing expected input/output
- **Guidelines**: Specific rules and best practices the agent should follow

## Best Practices for Agent Usage

1. **Be Specific**: Provide clear context and specific files/code to review
2. **One Task at a Time**: Focus agents on one area or task for best results
3. **Iterate**: Use feedback from agents to improve code, then re-review if needed
4. **Combine Agents**: Use multiple agents for comprehensive reviews (e.g., SRE + Italian Commenting)
5. **Document Findings**: Keep track of agent recommendations in issues or documentation

## Repository-Specific Context

The agents in this repository are aware of:
- Python applications (Flask web apps, utilities, ML scripts)
- Infrastructure as Code (Terraform for Azure/AWS, Docker Compose)
- Machine Learning experiments and Jupyter notebooks
- Multiple programming language examples
- Testing infrastructure (pytest)

## Support and Feedback

If you encounter issues with custom agents or have suggestions for improvements:
1. Open an issue describing the problem or enhancement
2. Tag the issue with `custom-agents` label
3. Provide specific examples of the behavior you observed

## References

- [GitHub Custom Agents Documentation](https://gh.io/customagents/config)
- [GitHub Copilot CLI](https://gh.io/customagents/cli)
- [SRE Principles and Practices](https://sre.google/)
- [Terraform Best Practices](https://www.terraform.io/docs/cloud/guides/recommended-practices/index.html)
- [Docker Security Best Practices](https://docs.docker.com/develop/security-best-practices/)
