# MCP

## Supported LLM's

* [Codex CLI ](https://chatgpt.com/features/codex)(recommended)
* [Cursor](https://cursor.com/home)
* [Claude Code](https://claude.com/product/claude-code)

## Installing

#### Codex CLI

For Codex CLI, we have a one-line install command which installs the MCP and guides you through setting up an MCP API key inside the Numerai Web App and applying the key to your environment variables.

You can install it using:

```bash
curl -sL http://numer.ai/install-mcp.sh | bash
```

If you prefer to manually install it, add this to the bottom of your `~/.codex/config.toml` :

```toml
[mcp_servers.numerai]
url = "https://api-tournament.numer.ai/mcp/sse"

[mcp_servers.numerai.env_http_headers]
Authorization = "NUMERAI_MCP_AUTH"
```

#### Cursor

Installing the MCP in cursor requires modifying the `~/.cursor/mcp.json` file, adding this configuration to the `mcpServers` object:

```json
{
  "mcpServers": {
    "numerai": {
      "url": "https://api-tournament.numer.ai/mcp/sse",
      "headers": {
        "Authorization": "Token ${env:NUMERAI_MCP_AUTH}"
      }
    }
  }
}
```

#### Claude Code

Installing the MCP to Claude Code also involves editing the `~/.config/claude/mcp.json` file:

```json
{
  "servers": {
    "numerai": {
      "transport": "sse",
      "url": "https://api-tournament.numer.ai/mcp/sse",
      "headers": {
        "Authorization": "Token ${NUMERAI_MCP_AUTH}"
      }
    }
  }
}
```

## Authenticating

Numerai MCP by leveraging the normal Numerai API Key which can be created by going to your [Account Settings](https://numer.ai/account) and scrolling down to the Automation section.

<figure><img src="https://1171682275-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LmGruQ_-ZYj9XMQUd5x%2Fuploads%2FbGk8Q48y4gxS5xteyvfX%2FScreenshot%202026-01-29%20at%201.05.48%E2%80%AFAM.png?alt=media&#x26;token=c5ce5ec8-2680-434f-a65f-fe6daf3bc96c" alt=""><figcaption></figcaption></figure>

We now have a new button for **Create MCP Key**, the only difference from a normal API key is we automatically select all of the scopes that are needed for the MCP to have full functionality. Currently, these scopes are:

* Upload submissions and pickled models
* Download previous submissions and pickled models
* View historical submission info
* View user info, (e.g. balance, withdrawal history)

Whether you are using a previously generated API key or creating a new MCP key, you will end up having a **PUBLIC\_KEY** and **PRIVATE\_KEY**. These need to be stored in an environment variable called `NUMERAI_MCP_AUTH` in the following format: `NUMERAI_MCP_AUTH="Token PUBLIC_KEY$PRIVATE_KEY"`&#x20;

This can be stored in your terminal environment using the following command:

```
export NUMERAI_MCP_AUTH="Token PUBLIC_KEY\$PRIVATE_KEY"
```

{% hint style="warning" %}
In many operating systems, the `$` character needs to be escaped. This is why in the above export command there is a `\$` between the public and private keys
{% endhint %}

## Usage

Once the MCP has been installed in your LLM of choice, using it simple. Your LLM should connect to it on startup automatically and you may begin using the tool using natural language.

Our tools are separated into two main categories: **tournament information** (get leaderboard, model performance, current round, etc.), and **research assistance** (creating and uploading models, checking on submissions, etc.)

We also have a generic GraphQL tool that will allow your LLM to utilize the introspection call to build it's own GraphQL calls and execute them through the MCP.
