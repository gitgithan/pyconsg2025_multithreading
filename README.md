# Talk Resources
- Slides in this repo: [pyconsg2025_deadlock.pdf](pyconsg2025_deadlock.pdf)
  - Links not clickable if viewing through github preview. Download for clickable links

- Video: https://www.youtube.com/watch?v=zuuOoAXKXQs

# Reproducing breakpoints
1. Install VSCode Extension: https://marketplace.visualstudio.com/items?itemName=deckerio.breakpointio
2. Ctrl+Shift+P and select `breakpoint-io: import`. This will import all breakpoints from .vscode/breakpoints.json that was exported using `breakpoint-io: export`
3. Your files should now have red dots in the gutter, and Debug Tab BREAKPOINTS section should be populated 

# Watch Variables
- self._shutdown
- _shutdown
- thread_module._shutdown
- _global_shutdown_lock.locked()
- self._work_queue.qsize()
- next(iter(list(_threads_queues.items())))[1].qsize()
- next(iter(list(thread_module._threads_queues.items())))[1].qsize()
