from fogger import log


log.info("Starting development server...")
log.success("Database connected successfully")
log.warning("Memory usage is getting high")
log.error("Failed to authenticate user")
log.question("Do you want to continue?")
log.debug("Loaded environment variables")

log.line()

log.set_format("{badge} → {message}")

log.success("Custom format enabled")

log.set_badge_style("[ {label:^8} ]")

log.info("New badge style applied")

log.line()

log.set_format("{time} {badge} {message}")

log.success("Fogger is running perfectly")